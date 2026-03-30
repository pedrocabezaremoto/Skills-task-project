## Context

Cataclysm: Dark Days Ahead (CDDA) is a turn-based survival game with a complex activity system that manages tasks for both the player and NPCs. Multi-activities (zone-based bulk tasks like farming, mining, construction, mopping, vehicle repair, etc.) are coordinated through `activity_handlers::resume_for_multi_activities()` and a backlog system where each sub-activity manually re-inserts the parent multi-activity into the character's backlog before returning.

## Problem Statement

Refactor the multi-activity backlogging mechanism to centralize and simplify how multi-activities resume after completing individual sub-tasks. Currently:

1. The function `activity_handlers::resume_for_multi_activities()` is called from many individual activity `finish()` methods (e.g., `chop_tree_activity_actor::finish`, `mop_activity_actor::finish`, `plant_seed_activity_actor::finish`, `churn_activity_actor::finish`, etc.) and even from non-multi-activity contexts, making the control flow scattered and hard to trace.

2. Each `multi_activity_do()` implementation manually inserts the parent multi-activity back into the character's backlog via `you.backlog.emplace_front(...)` before returning, creating repetitive boilerplate code across many activity types.

3. The `multi_zone_activity_actor::do_turn()` and `simulate_turn()` methods use an inconsistent cancellation-and-reassignment pattern on a per-turn basis rather than allowing multi-activities to auto-resume naturally.

4. The `out_of_moves()` helper function unnecessarily takes an `activity_id` parameter and reassigns the activity, when it should simply signal that the character is out of moves.

5. The `revert_npc_post_activity()` function applies NPC reversion logic even to the player character, which is incorrect.

## Requirements

- Remove all calls to `activity_handlers::resume_for_multi_activities()` from individual activity `finish()` methods and from `multi_activity_do()` implementations.
- Remove all manual `you.backlog.emplace_front(...)` insertions of the parent multi-activity from `multi_activity_do()` methods across all activity types.
- Modify `multi_zone_activity_actor::do_turn()` so that multi-activities auto-resume naturally instead of relying on per-turn cancellation and reassignment.
- Update `simulate_turn()` return values so that `true` consistently means "the activity should continue next turn" and `false` means "the activity is complete or was cancelled".
- Simplify `out_of_moves()` by removing the `activity_id` parameter.
- Fix `revert_npc_post_activity()` to only apply NPC-specific reversion logic to NPC characters.
- Ensure multi-activities are always assigned with `auto_resume = true` so they resume from the backlog automatically.
- Update the NPC activity loop to break when a destination is set.

## Success Criteria

- All existing tests tagged with `[construction]` must continue to pass without modification to test logic.
- Multi-activities (farming, mining, mopping, chopping, vehicle work, etc.) must correctly resume after individual sub-tasks complete for both player and NPC characters.
- No segfaults or infinite loops in the activity system.
- The codebase must have fewer lines of repetitive backlog management code.

## Relevant Files

- `src/activity_actor.cpp` — Contains `multi_zone_activity_actor::do_turn()`, `simulate_turn()`, and all individual activity actor `finish()` methods.
- `src/activity_actor_definitions.h` — Header with `simulate_turn()` declaration.
- `src/activity_item_handling.cpp` — Contains all `multi_activity_do()` implementations, `out_of_moves()`, `revert_npc_post_activity()`, and `route()` helper functions.
- `src/activity_item_handling.h` — Header for the above functions.
- `src/character.cpp` — Contains `assign_activity()` and `resume_backlog_activity()` methods.
- `src/npcmove.cpp` — Contains the NPC activity loop in `npc::do_player_activity()`.
- `tests/act_build_test.cpp` — Test file with construction-related test cases.

## Notes

- This is part of a larger multi-activity overhaul series. Only the changes described above are in scope.
- The refactoring must not alter game-visible behavior; activities must still complete successfully for both player and NPC characters.
- Do not modify the test framework or test assertions; only the source code under `src/` should be refactored.
