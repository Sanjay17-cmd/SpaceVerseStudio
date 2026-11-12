#include "SVCoordinateAdapter.h"
FVector USVCoordinateAdapter::ToUnrealPos(const FVector& SimPosKm) {
	return FVector(SimPosKm.X * 100000.0, -SimPosKm.Y * 100000.0, SimPosKm.Z * 100000.0);
}