
#include "SVSimulationSubsystem.h"

void USVSimulationSubsystem::SetSimulationState(
    const FSVSimulationState& State)
{
    if (State.EntityId.IsEmpty())
    {
        return;
    }

    EntStates.Add(State.EntityId, State);
    OnStateUpdated.Broadcast(State);
}

bool USVSimulationSubsystem::GetSimulationState(
    const FString& Id,
    FSVSimulationState& Out) const
{
    if (const FSVSimulationState* State = EntStates.Find(Id))
    {
        Out = *State;
        return true;
    }

    return false;
}
