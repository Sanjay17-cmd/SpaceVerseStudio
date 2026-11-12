#include "SVSimulationTestDriver.h"
#include "SVSimulationSubsystem.h"
#include "Engine/GameInstance.h"
#include "TimerManager.h"

ASVSimulationTestDriver::ASVSimulationTestDriver()
{
    PrimaryActorTick.bCanEverTick = false;
}

void ASVSimulationTestDriver::BeginPlay()
{
    Super::BeginPlay();
    GetWorldTimerManager().SetTimer(TelemetryTimer, this, &ASVSimulationTestDriver::PublishTestTelemetry, 1.0f, true);
}

void ASVSimulationTestDriver::PublishTestTelemetry()
{
    if (!GetGameInstance()) return;
    auto* Simulation = GetGameInstance()->GetSubsystem<USVSimulationSubsystem>();
    if (!Simulation) return;

    FSVSimulationState State;
    State.EntityId = TEXT("TestSpacecraft");
    State.PositionKm = FVector(7000.0 + Sequence, 0.0, 0.0);
    State.VelocityKmPerSec = FVector(0.0, 7.5, 0.0);
    State.SimulationTimeSeconds = Sequence;
    State.SequenceNumber = Sequence;

    Simulation->SetSimulationState(State);
    UE_LOG(LogTemp, Display, TEXT("TEST TELEMETRY | Sequence: %lld | Position: %s"), Sequence, *State.PositionKm.ToString());
    Sequence++;
}