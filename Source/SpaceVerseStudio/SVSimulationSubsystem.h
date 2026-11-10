
#pragma once

#include "CoreMinimal.h"
#include "Subsystems/GameInstanceSubsystem.h"
#include "SVSimulationSubsystem.generated.h"

USTRUCT(BlueprintType)
struct FSVSimulationState
{
    GENERATED_BODY()

    UPROPERTY(BlueprintReadWrite, Category = "Simulation")
    FVector PositionKm = FVector::ZeroVector;

    UPROPERTY(BlueprintReadWrite, Category = "Simulation")
    FVector VelocityKmPerSec = FVector::ZeroVector;

    UPROPERTY(BlueprintReadWrite, Category = "Simulation")
    FQuat Attitude = FQuat::Identity;

    UPROPERTY(BlueprintReadWrite, Category = "Simulation")
    double SimulationTimeSeconds = 0.0;

    UPROPERTY(BlueprintReadWrite, Category = "Simulation")
    int64 SequenceNumber = 0;
};

DECLARE_DYNAMIC_MULTICAST_DELEGATE_OneParam(
    FOnSimulationStateUpdated,
    FSVSimulationState, NewState
);

UCLASS()
class SPACEVERSESTUDIO_API USVSimulationSubsystem
    : public UGameInstanceSubsystem
{
    GENERATED_BODY()

public:
    UPROPERTY(BlueprintAssignable, Category = "Simulation")
    FOnSimulationStateUpdated OnStateUpdated;

    UFUNCTION(BlueprintCallable, Category = "Simulation")
    void SetSimulationState(const FSVSimulationState& NewState);

    UFUNCTION(BlueprintPure, Category = "Simulation")
    FSVSimulationState GetSimulationState() const;

private:
    UPROPERTY()
    FSVSimulationState CurrentState;
};
