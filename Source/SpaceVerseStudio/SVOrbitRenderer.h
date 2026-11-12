#pragma once
#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Components/SplineComponent.h"
#include "SVOrbitRenderer.generated.h"
UCLASS()
class SPACEVERSESTUDIO_API ASVOrbitRenderer :public AActor {
	GENERATED_BODY()
public:
	ASVOrbitRenderer();
	UPROPERTY(VisibleAnywhere)
	USplineComponent* sp;
	UFUNCTION(BlueprintCallable)
	void AddPt(FVector pt);
};