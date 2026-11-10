
#include "SVWorldManager.h"
#include "SVSpacecraftActor.h"
#include "EngineUtils.h"

ASVWorldManager::ASVWorldManager()
{
    PrimaryActorTick.bCanEverTick = false;
}

void ASVWorldManager::BeginPlay()
{
    Super::BeginPlay();

    if (!GetGameInstance())
    {
        UE_LOG(LogTemp, Error, TEXT("GameInstance unavailable"));
        return;
    }

    SimulationSubsystem =
        GetGameInstance()->GetSubsystem<USVSimulationSubsystem>();

    if (!SimulationSubsystem)
    {
        UE_LOG(LogTemp, Error, TEXT("SimulationSubsystem unavailable"));
        return;
    }

    for (TActorIterator<ASVSpacecraftActor> It(GetWorld()); It; ++It)
    {
        SpacecraftActors.Add(*It);
    }

    SimulationSubsystem->OnStateUpdated.AddDynamic(
        this, &ASVWorldManager::HandleSimulationStateUpdated);

    UE_LOG(LogTemp, Display,
        TEXT("World Manager initialized. Spacecraft: %d"),
        SpacecraftActors.Num());
}

void ASVWorldManager::EndPlay(
    const EEndPlayReason::Type EndPlayReason)
{
    if (SimulationSubsystem)
    {
        SimulationSubsystem->OnStateUpdated.RemoveDynamic(
            this, &ASVWorldManager::HandleSimulationStateUpdated);
    }

    Super::EndPlay(EndPlayReason);
}

void ASVWorldManager::HandleSimulationStateUpdated(
    FSVSimulationState NewState)
{
    for (ASVSpacecraftActor* Spacecraft : SpacecraftActors)
    {
        if (IsValid(Spacecraft))
        {
            Spacecraft->UpdateTelemetryState(NewState);
        }
    }
}
