#include "SVOrbitRenderer.h"
ASVOrbitRenderer::ASVOrbitRenderer() {
	PrimaryActorTick.bCanEverTick = false;
	sp = CreateDefaultSubobject<USplineComponent>("sp");
	RootComponent = sp;
}
void ASVOrbitRenderer::AddPt(FVector pt) {
	sp->AddSplinePoint(pt, ESplineCoordinateSpace::World);
}