#pragma once
#include "CoreMinimal.h"
#include "Kismet/BlueprintFunctionLibrary.h"
#include "SVCoordinateAdapter.generated.h"
UCLASS()
class SPACEVERSESTUDIO_API USVCoordinateAdapter : public UBlueprintFunctionLibrary {
	GENERATED_BODY()
public:
	UFUNCTION(BlueprintPure, Category = "Sim|Coords")
	static FVector ToUnrealPos(const FVector& SimPosKm);
};