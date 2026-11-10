
#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "SVSimulationSubsystem.h"
#include "SVWorldManager.generated.h"

class ASVSpacecraftActor;

UCLASS()
class SPACEVERSESTUDIO_API ASVWorldManager : public AActor
{
    GENERATED_BODY()

public:
    ASVWorldManager();

protected:
    virtual void BeginPlay() override;
    virtual void EndPlay(const EEndPlayReason::Type EndPlayReason) override;

private:
    UPROPERTY()
    TArray<TObjectPtr<ASVSpacecraftActor>> SpacecraftActors;

    UPROPERTY()
    TObjectPtr<USVSimulationSubsystem> SimulationSubsystem;

    UFUNCTION()
    void HandleSimulationStateUpdated(FSVSimulationState NewState);
};
