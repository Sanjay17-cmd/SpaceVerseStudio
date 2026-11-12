"""Command-line client that validates and displays streamed mock snapshots."""
from __future__ import annotations

import argparse

import grpc

from spaceverse.v1 import simulation_pb2 as pb
from spaceverse.v1 import simulation_pb2_grpc as pb_grpc
from spaceverse_mock.validation import validate_snapshot


def main() -> None:
    parser = argparse.ArgumentParser(description="Read SpaceVerse telemetry snapshots")
    parser.add_argument("--target", default="127.0.0.1:50051")
    parser.add_argument("--run-id", default="spaceverse-local-mock-run-001")
    parser.add_argument("--entity-id", action="append", dest="entity_ids")
    parser.add_argument("--count", type=int, default=10)
    parser.add_argument("--interval-ms", type=int, default=500)
    args = parser.parse_args()

    if args.count < 1 or args.count > 10000:
        parser.error("--count must be between 1 and 10000")
    if args.interval_ms < 20 or args.interval_ms > 60000:
        parser.error("--interval-ms must be between 20 and 60000")

    request = pb.StreamStateRequest(
        run_id=args.run_id,
        entity_ids=args.entity_ids or ["terra-001"],
        max_updates=args.count,
        interval_ms=args.interval_ms,
        client_name="SpaceVerseIntegrationSandbox-CLI",
    )

    with grpc.insecure_channel(args.target) as channel:
        stub = pb_grpc.SimulationTelemetryServiceStub(channel)
        timeout = args.count * args.interval_ms / 1000.0 + 15.0
        stream = stub.StreamStateSnapshots(request, timeout=timeout)
        received = 0
        last_sequence_by_entity: dict[str, int] = {}
        last_time_by_entity: dict[str, float] = {}
        for snapshot in stream:
            validate_snapshot(snapshot)
            previous_sequence = last_sequence_by_entity.get(snapshot.entity_id)
            previous_time = last_time_by_entity.get(snapshot.entity_id)
            if previous_sequence is not None and snapshot.sequence_number <= previous_sequence:
                raise RuntimeError(f"Non-increasing sequence for {snapshot.entity_id}")
            if previous_time is not None and snapshot.simulation_time.elapsed_seconds <= previous_time:
                raise RuntimeError(f"Non-increasing simulation time for {snapshot.entity_id}")
            last_sequence_by_entity[snapshot.entity_id] = snapshot.sequence_number
            last_time_by_entity[snapshot.entity_id] = snapshot.simulation_time.elapsed_seconds
            print(
                f"run={snapshot.run_id} entity={snapshot.entity_id} "
                f"seq={snapshot.sequence_number} "
                f"t={snapshot.simulation_time.elapsed_seconds:.3f}s "
                f"r_km=({snapshot.position.x:.3f}, {snapshot.position.y:.3f}, {snapshot.position.z:.3f}) "
                f"v_km_s=({snapshot.velocity.x:.6f}, {snapshot.velocity.y:.6f}, {snapshot.velocity.z:.6f}) "
                f"frame={snapshot.custom_reference_frame}"
            )
            received += 1
        if received == 0:
            raise RuntimeError("No telemetry snapshots received")
        print(f"PASS: received and validated {received} snapshot(s)")


if __name__ == "__main__":
    main()
