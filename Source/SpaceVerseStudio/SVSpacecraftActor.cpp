
#include "SVSpacecraftActor.h"
#include "Components/StaticMeshComponent.h"

ASVSpacecraftActor::ASVSpacecraftActor()
{
    PrimaryActorTick.bCanEverTick = false;

    SpacecraftMesh = CreateDefaultSubobject<UStaticMeshComponent>(
        TEXT("SpacecraftMesh"));

    SetRootComponent(SpacecraftMesh);
}

void ASVSpacecraftActor::UpdateTelemetryState(
    const FSVSimulationState& NewState)
{
    TelemetryState = NewState;
}

FSVSimulationState ASVSpacecraftActor::GetTelemetryState() const
{
    return TelemetryState;
}
