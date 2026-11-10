
#include "SVSimulationSubsystem.h"

void USVSimulationSubsystem::SetSimulationState(
    const FSVSimulationState& NewState)
{
    CurrentState = NewState;
    OnStateUpdated.Broadcast(CurrentState);
}

FSVSimulationState USVSimulationSubsystem::GetSimulationState() const
{
    return CurrentState;
}
