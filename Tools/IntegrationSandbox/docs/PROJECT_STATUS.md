# Project status at sandbox creation

- Unreal Engine project: `SpaceVerseStudio` (UE 5.8, Windows).
- Existing Unreal-side classes reported by the developer: `SVSpacecraftActor`, `SVWorldManager`, `SVSimulationSubsystem`, plus a temporary telemetry driver.
- Visual Terra GLB scene import is complete; the imported scene contains multiple mesh actors and material instances.
- The current Unreal prototype's state structure was originally single-state and is not yet a production multi-entity transport contract.
- This sandbox adds a versioned protobuf contract and Python mock producer/client/tests. It intentionally does not modify the Unreal module or add an unverified third-party gRPC C++ dependency.

## Next Unreal-side integration work

1. Review and approve the v1 proto with the runtime team.
2. Add a dedicated Unreal transport adapter using an agreed UE 5.8-compatible gRPC/protobuf dependency strategy.
3. Add per-entity snapshot storage and sequence validation to `SVSimulationSubsystem`.
4. Add a tested coordinate adapter after frame, axes, units, time scale and quaternion convention are signed off.
5. Add render interpolation that never feeds back into authoritative simulation state.
6. Replace the temporary in-process telemetry driver with the external gRPC stream.
