# Schema and compatibility policy

1. The authoritative schema is `proto/spaceverse/v1/simulation.proto`.
2. Package path `kepler.spaceverse.v1` is a versioned API namespace.
3. Never change or reuse an existing protobuf field number.
4. When deleting a field, reserve its number and name in the next schema revision.
5. Prefer additive optional fields for backward-compatible changes.
6. A breaking contract change requires a new package namespace such as `v2`, coordinated producer/consumer migration, fixtures, and tests.
7. Consumers must reject unspecified units, reference frames, axis conventions, and attitude conventions. Do not infer them.
8. `sequence_number` is monotonic per entity within a run. A consumer should detect duplicates, gaps, and out-of-order updates.
9. `simulation_time.elapsed_seconds` is relative to the run epoch. `epoch_julian_date` is populated only when the producer supplies a valid absolute epoch and explicit time scale.
10. Quaternion fields are always `x,y,z,w`; the attitude convention defines rotation direction. Consumers validate normalization.
11. The mock's custom frame and trajectory are test-only. They must never be labelled J2000/ICRF or treated as mission truth.

12. `is_valid` is a producer quality flag only. It does not mean flight-qualified, independently verified, or scientifically validated.
