# Base definition of ability class

class Ability:
    abilityID: int = 0
    abilityName: str = ""
    abilityDescription: str = ""
    
    # Priority determines the order in which abilities are computed
    # Higher priority abilities are computed first
    # Priority 0 is reserved for basic attacks
    # Abilities with same priority are computed in the order of increasing abilityID
    priority: int = 0
    
    # Cooldowns
    cooldown: float = 0.0
    cooldownRemaining: float = 0.0
    
    # Resource costs
    # Resources can be mana, energy, fury, blood, etc.
    # Defined as a dictionary with level as key and cost as value
    # Values between levels are determined based on resourceGrowthMethod variable
    resourceCosts: dict[int, float] = {
        0: 0.0,
    }
    
    # Resource growth method
    # Determines how resource costs increase with level in between the levels defined in resourceCosts
    # Options: "linear", "step"
    # Default: "step"
    resourceGrowthMethod: str = "step"
    
    def __init__(self):
        # Initializes the ability object
        pass
    
    def computeAbility(self, champion):
        # Computes the ability
        # champion: Champion object
        pass
    
    def useAbility(self, champion):
        # Uses the ability
        # champion: Champion object
        pass
    
    def levelUp(self):
        # Levels up the ability
        pass
    
    def resetCooldown(self):
        # Resets the cooldown of the ability
        pass