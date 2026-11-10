
#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "SVSimulationSubsystem.h"
#include "SVSpacecraftActor.generated.h"

UCLASS()
class SPACEVERSESTUDIO_API ASVSpacecraftActor : public AActor
{
    GENERATED_BODY()

public:
    ASVSpacecraftActor();

    UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Spacecraft")
    TObjectPtr<UStaticMeshComponent> SpacecraftMesh;

    UFUNCTION(BlueprintCallable, Category = "Spacecraft")
    void UpdateTelemetryState(const FSVSimulationState& NewState);

    UFUNCTION(BlueprintPure, Category = "Spacecraft")
    FSVSimulationState GetTelemetryState() const;

private:
    UPROPERTY(VisibleAnywhere, Category = "Spacecraft")
    FSVSimulationState TelemetryState;
};
