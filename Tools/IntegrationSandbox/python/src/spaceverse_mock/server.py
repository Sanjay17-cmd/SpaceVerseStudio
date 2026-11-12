"""Local gRPC mock telemetry server. Ctrl+C stops the server."""
from __future__ import annotations

import argparse
import logging
import math
import time
from concurrent import futures

import grpc

from spaceverse.v1 import simulation_pb2 as pb
from spaceverse.v1 import simulation_pb2_grpc as pb_grpc
from spaceverse_mock.model import MOCK_ENTITIES, MOCK_RUN_ID, make_snapshot
from spaceverse_mock.validation import validate_snapshot


class SimulationTelemetryService(pb_grpc.SimulationTelemetryServiceServicer):
    def StreamStateSnapshots(self, request, context):
        run_id = request.run_id.strip() or MOCK_RUN_ID
        entity_ids = list(request.entity_ids) if request.entity_ids else ["terra-001"]
        if request.interval_ms == 0:
            interval_ms = 1000
        else:
            interval_ms = int(request.interval_ms)
        if interval_ms < 20 or interval_ms > 60000:
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, "interval_ms must be between 20 and 60000")
        unknown = [entity_id for entity_id in entity_ids if entity_id not in MOCK_ENTITIES]
        if unknown:
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, f"Unknown entity_ids: {unknown}")
        if len(set(entity_ids)) != len(entity_ids):
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, "entity_ids must not contain duplicates")

        max_updates = int(request.max_updates)  # 0 means unlimited
        if max_updates > 10000:
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, "max_updates cannot exceed 10000")

        sequence = 0
        while context.is_active() and (max_updates == 0 or sequence < max_updates):
            elapsed = sequence * interval_ms / 1000.0
            for entity_id in entity_ids:
                snapshot = make_snapshot(entity_id, sequence, elapsed, run_id)
                validate_snapshot(snapshot)
                yield snapshot
            sequence += 1
            if max_updates == 0 or sequence < max_updates:
                time.sleep(interval_ms / 1000.0)

    def GetLatestState(self, request, context):
        entity_id = request.entity_id.strip()
        if entity_id not in MOCK_ENTITIES:
            context.abort(grpc.StatusCode.NOT_FOUND, f"Unknown entity_id: {entity_id}")
        run_id = request.run_id.strip() or MOCK_RUN_ID
        snapshot = make_snapshot(entity_id, 0, 0.0, run_id)
        validate_snapshot(snapshot)
        return snapshot


def main() -> None:
    parser = argparse.ArgumentParser(description="SpaceVerse local mock gRPC telemetry server")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=50051)
    args = parser.parse_args()

    if not (1 <= args.port <= 65535):
        parser.error("--port must be between 1 and 65535")

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=8))
    pb_grpc.add_SimulationTelemetryServiceServicer_to_server(
        SimulationTelemetryService(), server
    )
    address = f"{args.host}:{args.port}"
    if server.add_insecure_port(address) == 0:
        raise RuntimeError(f"Could not bind gRPC server to {address}")

    server.start()
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    logging.info("SpaceVerse MOCK telemetry server listening on %s", address)
    logging.info("Entities: %s", ", ".join(MOCK_ENTITIES))
    logging.info("This is synthetic demonstration data, not flight/mission truth.")
    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        logging.info("Stopping mock telemetry server...")
        server.stop(grace=1).wait()


if __name__ == "__main__":
    main()
