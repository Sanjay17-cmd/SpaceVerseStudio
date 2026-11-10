#pragma once
#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "SVSimulationTestDriver.generated.h"

UCLASS()
class SPACEVERSESTUDIO_API ASVSimulationTestDriver : public AActor
{
    GENERATED_BODY()
public:
    ASVSimulationTestDriver();
protected:
    virtual void BeginPlay() override;
private:
    void PublishTestTelemetry();
    FTimerHandle TelemetryTimer;
    int64 Sequence = 0;
};