# SpaceVerse Integration Sandbox (v0.1.0)

A temporary, self-contained contract and mock-data codebase for developing the Unreal/runtime integration before the runtime team supplies its implementation.

## What is included

- `proto/spaceverse/v1/simulation.proto`: versioned Protocol Buffers + gRPC service contract.
- `python/`: deterministic mock gRPC producer, CLI client, protobuf validation, tests, and Windows PowerShell setup/run scripts.
- `fixtures/sample_snapshot.json`: one example snapshot using the same v1 schema.
- `docs/`: schema evolution policy and planned Unreal integration boundary.
- `unreal/`: reserved for Unreal adapter documentation and future implementation files.

## Important scope statement

This is a development/test contract, not a flight-qualified interface and not a substitute for the runtime team's approved ICD. The mock trajectory is a simple circular two-body demonstration in an explicitly custom test frame. It is not a validated mission trajectory, does not include perturbations, and is not J2000/ICRF. The snapshot `is_valid` flag means only that the mock considers that record structurally usable; it is not a flight-qualification claim. Do not use it as scientific ground truth.

## Install on Windows

Prerequisites: Python 3.11+ and PowerShell.

1. Open PowerShell in this folder's `python` directory.
2. Run:

   ```powershell
   Set-ExecutionPolicy -Scope Process Bypass
   .\setup.ps1
   ```

This creates `.venv`, installs dependencies, and generates Python protobuf/gRPC stubs from the single `.proto` source.

## Run the contract tests

```powershell
.\run_tests.ps1
```

Expected: 5 tests pass.

## Run the mock server and client

Terminal 1:

```powershell
.\run_server.ps1
```

Terminal 2 (same `python` folder):

```powershell
.\run_client.ps1
```

Expected: 10 validated snapshots for `terra-001`, with increasing sequence numbers and elapsed simulation time. To test the second entity:

```powershell
.\run_client.ps1 -EntityId demo-sat-002 -Count 10 -IntervalMs 250
```

Stop the server with Ctrl+C.

## Generate stubs after editing the proto

```powershell
.\scripts\generate_stubs.ps1
```

Never hand-edit generated `_pb2.py`, `_pb2_grpc.py`, `.pyi`, or future C++ generated files.

## Move into the main Unreal repository

Recommended location: `Tools/IntegrationSandbox/` at the root of `SpaceVerseStudio`, outside `Content/`. This keeps schemas and Python tooling out of Unreal's cooked content while keeping them in the same Git codebase.

## Contract evolution

Read `docs/SCHEMA_POLICY.md` before changing the `.proto`. Never reuse field numbers. Breaking changes require a new package version.
