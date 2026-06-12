import random

WORLD_CUP_DB = {
    "Group A": {
        "Mexico": {"rating": 81, "morale": 80},
        "South Korea": {"rating": 78, "morale": 75},
        "Czechia": {"rating": 76, "morale": 70},
        "South Africa": {"rating": 72, "morale": 70}
    },
    "Group B": {
        "Canada": {"rating": 77, "morale": 80},
        "Switzerland": {"rating": 79, "morale": 75},
        "Qatar": {"rating": 71, "morale": 70},
        "Bosnia and Herzegovina": {"rating": 74, "morale": 70}
    },
    "Group C": {
        "Brazil": {"rating": 89, "morale": 85},
        "Morocco": {"rating": 82, "morale": 80},
        "Scotland": {"rating": 76, "morale": 75},
        "Haiti": {"rating": 68, "morale": 65}
    },
    "Group D": {
        "USA": {"rating": 80, "morale": 85},
        "Paraguay": {"rating": 75, "morale": 70},
        "Australia": {"rating": 76, "morale": 75},
        "Türkiye": {"rating": 78, "morale": 75}
    },
    "Group L": {
        "England": {"rating": 88, "morale": 80},
        "Croatia": {"rating": 82, "morale": 75},
        "Ghana": {"rating": 75, "morale": 75},
        "Panama": {"rating": 71, "morale": 70}
    }
}

def load_team():
    print("\n" "=== 2026 FIFA WORLD CUP QUALIFIED COUNTRIES ===") 
    print("\n""Welcome to the FIFA 2026 World Cup Manager Simulator!")
    print("\n""Available Groups & Teams:")
    for group, teams in WORLD_CUP_DB.items():
        print("\n"f" {group}:  =  {', '.join(teams.keys())}")
        
    while True:
        choice = input("\nSelect your National Team to manage: ").strip()
        for group, teams in WORLD_CUP_DB.items():
            if choice in teams:
                return choice, group, teams[choice]
        print("Error: Team not found in 2026 database. Please check spelling.")

def play_match(team_name, my_stats, opponent_name, opponent_rating, match_type="Group"):
    print(f"\n⚽ MATCHDAY: {team_name} vs {opponent_name} ({match_type} Stage)")
    
    # Calculate performance index out of 300 max
    my_power = (my_stats["rating"] + my_stats["morale"] + my_stats["fitness"]) / 3
    opp_power = opponent_rating
    
    # Win calculation logic
    win_margin = my_power - opp_power
    roll = random.randint(-20, 20)
    total_score = win_margin + roll
    
    if total_score > 5:
        print(f"🎉 Result: {team_name} WINS against {opponent_name}!")
        return "win"
    elif total_score < -5:
        print(f"💔 Result: {team_name} LOSES to {opponent_name}!")
        return "loss"
    else:
        if match_type == "Knockout":
            # Extra time / penalties resolver for knockouts
            knockout_winner = random.choice(["win", "loss"])
            print(f"⏱️ Deep into Extra Time! {team_name} " + ("WINS on Penalties!" if knockout_winner == "win" else "LOSES on Penalties!"))
            return knockout_winner
        print(f"🤝 Result: A hard-fought DRAW between {team_name} and {opponent_name}.")
        return "draw"

def run_simulation():
    team, group_name, stats = load_team()
    my_team_stats = {
        "rating": stats["rating"],
        "morale": stats["morale"],
        "fitness": 90  # Initial physical condition percentage
    }
    
    # Identify group opponents dynamically from database
    opponents = [opp for opp in WORLD_CUP_DB[group_name].keys() if opp != team]
    
    # --- LOOP 1: PRE-TOURNAMENT HUB (Using 'continue' and 'pass') ---
    print(f"\n--- Pre-Tournament Training Camp: Managing {team} ---")
    weeks_left = 2
    while weeks_left > 0:
        print(f"\n[Preparation Week {weeks_left}] Status -> Rating: {my_team_stats['rating']} | Morale: {my_team_stats['morale']} | Fitness: {my_team_stats['fitness']}")
        action = input("Select preparation focal point ('tactics', 'rest', 'scout'): ").strip().lower()
        
        if action == 'tactics':
            my_team_stats["rating"] = min(100, my_team_stats["rating"] + 4)
            my_team_stats["fitness"] = max(40, my_team_stats["fitness"] - 10)
            weeks_left -= 1
        elif action == 'rest':
            my_team_stats["fitness"] = min(100, my_team_stats["fitness"] + 15)
            my_team_stats["morale"] = min(100, my_team_stats["morale"] + 5)
            weeks_left -= 1
        elif action == 'scout':
            # Assignment Rule: pass statement placeholder for future opposition profiling analysis systems
            print("Running basic opposition data scanning maps...")
            pass 
            continue  # Skips decrementing weeks_left, letting the manager try an action again
        else:
            print("Invalid staff order. Week wasted.")
            weeks_left -= 1

    # --- LOOP 2: REALISTIC GROUP STAGE SIMULATION ---
    print("\n--- Phase 2: FIFA 2026 Group Stage Commences ---")
    group_points = 0
    match_index = 0
    
    while match_index < len(opponents):
        opp = opponents[match_index]
        opp_rating = WORLD_CUP_DB[group_name][opp]["rating"]
        
        res = play_match(team, my_team_stats, opp, opp_rating, match_type="Group")
        
        if res == "win":
            group_points += 3
            my_team_stats["morale"] = min(100, my_team_stats["morale"] + 8)
        elif res == "draw":
            group_points += 1
            my_team_stats["morale"] = min(100, my_team_stats["morale"] + 2)
        else:
            my_team_stats["morale"] = max(10, my_team_stats["morale"] - 10)
            
        # Realistic Injury Event Handling
        if random.random() < 0.30:
            print("🚨 INJURY BLOW: Medical staff reports a key starter pulled a muscle!")
            my_team_stats["fitness"] = max(30, my_team_stats["fitness"] - 20)
            match_index += 1
            continue  # Skip regular fitness regeneration window for match post-processing
            
        my_team_stats["fitness"] = min(100, my_team_stats["fitness"] - 5)
        match_index += 1

    print(f"\n📊 Group Phase Concluded. {team} finished with {group_points} points.")
    if group_points < 4:
        print(f"❌ {team} fails to secure a top-2 spot and is knocked out of the World Cup.")
        return

    # --- LOOP 3: BRUTAL KNOCKOUT BRACKET ---
    print("\n✅ Progression Secured! Entering the Knockout Stages.")
    knockout_stages = ["Round of 16", "Quarter-Final", "Semi-Final", "Championship Final"]
    stage_idx = 0
    
    while stage_idx < len(knockout_stages):
        stage = knockout_stages[stage_idx]
        print(f"\n🏆 {stage.upper()} MATCHUP")
        
        # Draw realistic opponent profile from outside your group
        giant_teams = ["Brazil", "England", "Spain", "Germany", "Morocco", "Switzerland"]
        opp = random.choice([t for t in giant_teams if t != team])
        opp_rating = 83 + (stage_idx * 3) # Opponents scale up in difficulty per round
        
        res = play_match(team, my_team_stats, opp, opp_rating, match_type="Knockout")
        
        if res == "win":
            print(f"👍 Sensational! {team} advances from the {stage}!")
            my_team_stats["morale"] = min(100, my_team_stats["morale"] + 12)
            stage_idx += 1
        else:
            print(f"❌ Devastation. {team} has been eliminated in the {stage}.")
            break  # Assignment Rule: Instantly exit the simulation loop on knockout failure

    if stage_idx == len(knockout_stages):
        print(f"\n🏆👑 WORLD CHAMPIONS! {team} conquered the 2026 FIFA World Cup! 👑🏆")

if __name__ == "__main__":
    run_simulation()
