# Base definition of champion class

from league_of_agents.abilities.ability import Ability

class Champion:
    # Defines the several attributes and methods needed for champions
    
    championID: int = 0
    championName: str = ""
    
    # Base stats
    # All growth stats are per level
    # All regen stats are per second
    # All distance stats are in "units"
    baseHealth: float = 0.0
    healthGrowth: float = 0.0
    baseHealthRegen: float = 0.0
    healthRegenGrowth: float = 0.0
    
    baseAttackDamage: float = 0.0
    attackDamageGrowth: float = 0.0
    baseAbilityPower: float = 0.0
    abilityPowerGrowth: float = 0.0
    
    baseArmor: float = 0.0
    armorGrowth: float = 0.0
    baseMagicResist: float = 0.0
    magicResistGrowth: float = 0.0
    
    # Resource stats
    # Resources are known as mana, energy, fury, blood, etc. in League of Legends
    baseResource: float = 0.0
    resourceGrowth: float = 0.0
    baseResourceRegen: float = 0.0
    resourceRegenGrowth: float = 0.0
    
    baseAttackSpeed: float = 0.0
    attackSpeedGrowth: float = 0.0
    
    baseMoveSpeed: float = 0.0
    
    attackRange: float = 0.0
    
    currentHealth: float = 0.0
    currentResource: float = 0.0
    
    currentPosition: tuple[float, float] = (0.0, 0.0)
    
    currentLevel: int = 0
    
    # Abilities
    abilities: list[Ability] = []
    
    def __init__(self):
        # Initializes the champion object
        pass
    
    def levelUp(self):
        # Levels up the champion
        self.currentLevel += 1
        
        self.currentHealth += self.healthGrowth
        self.currentResource += self.resourceGrowth
        
    def currentAttackDamage(self):
        # Returns the current attack damage of the champion
        return self.baseAttackDamage + self.currentLevel * self.attackDamageGrowth
    
    def currentAbilityPower(self):
        # Returns the current ability power of the champion
        return self.baseAbilityPower + self.currentLevel * self.abilityPowerGrowth
    
    def currentArmor(self):
        # Returns the current armor of the champion
        return self.baseArmor + self.currentLevel * self.armorGrowth
    
    def currentMagicResist(self):
        # Returns the current magic resist of the champion
        return self.baseMagicResist + self.currentLevel * self.magicResistGrowth
    
    def currentAttackSpeed(self):
        # Returns the current attack speed of the champion
        return self.baseAttackSpeed + self.currentLevel * self.attackSpeedGrowth
