class Enemy:

    
    def __init__(self, name, hp, attack, defense, xp_reward, description):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.xp_reward = xp_reward
        self.description = description
    
    def take_damage(self, amount):

        self.hp -= amount
        if self.hp < 0:
            self.hp = 0
    
    def is_alive(self):
        return self.hp > 0
    
    def get_attack_damage(self):
        return self.attack


class 43(Enemy):
    
    def __init__(self):
        super().__init__(
            name="Goblin",
            hp=50,          # ← 30 → 50 (mais resistente)
            attack=15,      # ← 6 → 10 → 15 (mais forte)
            defense=2,      # ← 2 → 4 (mais difícil de acertar)
            xp_reward=120,
            description="Um goblin pequeno, mas rápido, segura uma lâmina enferrujada."
        )
        self.can_flee = True


class OrcChief(Enemy):
    
    def __init__(self):
        super().__init__(
            name="Orc Chief",
            hp=90,
            attack=28,
            defense=7,
            xp_reward=180,
            description="Um orc enorme bloqueia a passagem, com cicatrizes de batalhas antigas."
        )
        self.can_flee = False
        self.turn_counter = 0
    
    def get_attack_damage(self):
        self.turn_counter += 1
        
        if self.turn_counter % 3 == 0:
            print(f"\n⚠️  {self.name} usa ATAQUE PODEROSO!")
            return self.attack * 2
        
        return self.attack


class MestreButcher(Enemy):
    """Chefe de cozinha esqueleto que ataca invasores"""
    
    def __init__(self):
        super().__init__(
            name="Mestre Butcher",
            hp=80,
            attack=20,
            defense=5,
            xp_reward=150,
            description="Um chefe de cozinha incrível que agora é só um esqueleto, porém ele ataca quem entra na cozinha dele."
        )
        self.can_flee = True
        self.turn_counter = 0
    
    def get_attack_damage(self):
        self.turn_counter += 1
        
        if self.turn_counter % 4 == 0:
            print(f"\n🔪 {self.name} arremessa facas de açougueiro!")
            return int(self.attack * 1.5)
        
        return self.attack


class Spaghettus(Enemy):
    """Macarrão vivo criado pelo Mestre Butcher"""
    
    def __init__(self):
        super().__init__(
            name="Spaghettus",
            hp=45,
            attack=12,
            defense=2,
            xp_reward=89,
            description="Um macarrão que ganhou vida graças ao Mestre Butcher."
        )
        self.can_flee = True


class Blackwarrior(Enemy):
    """Guerreiro sombrio invocável no Altar"""
    
    def __init__(self):
        super().__init__(
            name="Blackwarrior",
            hp=100,
            attack=25,
            defense=8,
            xp_reward=250,
            description="Um guerreiro sombrio que protege os segredos do altar."
        )
        self.can_flee = False
        self.turn_counter = 0
    
    def get_attack_damage(self):
        self.turn_counter += 1
        
        if self.turn_counter % 3 == 0:
            print(f"\n⚫ 💥 {self.name} libera sua FÚria Sombria!")
            return int(self.attack * 2.5)
        
        return self.attack

class Necromancer(Enemy):
    """Necromante que usa magias sombrias"""
    
    def __init__(self):
        super().__init__(
            name="Necromante",
            hp=120,
            attack=22,
            defense=6,
            xp_reward=300,
            description="Um necromante poderoso envolto em vestes sombrias. Ossos flutuam ao seu redor."
        )
        self.can_flee = False
        self.turn_counter = 0
    
    def get_attack_damage(self):
        self.turn_counter += 1
        
        if self.turn_counter % 3 == 0:
            print(f"\n💀 {self.name} lança DRENAGEM DE ALMA!")
            print(f"⚫ Você sente sua força vital sendo sugada!")
            # Dano 2x e cura o necromante em 20% do dano causado
            damage = int(self.attack * 2)
            heal_amount = int(damage * 0.2)
            self.hp = min(self.hp + heal_amount, self.max_hp)
            if heal_amount > 0:
                print(f"💚 {self.name} recuperou {heal_amount} HP!")
            return damage
        
        return self.attack

class esqueleto(Enemy):
    """Esqueleto reanimado pelo Necromante"""
    
    def __init__(self):
        super().__init__(
            name="Esqueleto",
            hp=60,
            attack=16,
            defense=4,
            xp_reward=100,
            description="Um esqueleto reanimado que serve ao necromante."
        )
        self.can_flee = True

class PrisionGuard(Enemy):
    """O Guarda de prisão corrompido"""
    
    def __init__(self):
        super().__init__(
            name="O Guarda de Prisão Corrompido",
            hp=80,
            attack=19,
            defense=6,
            xp_reward=150,
            description="Um guarda de prisão que foi corrompido."
        )
        self.can_flee = True

class Shadowmage(Enemy):
    """mago das sombras que habita as câmara"""
    
    def __init__(self):
        super().__init__(
            name="mago das Sombras",
            hp=90,
            attack=15,
            defense=4,
            xp_reward=220,
            description="Um mago das sombras que se move nas sombras das câmara."
        )
        self.can_flee = False

class Dragonwarrior(Enemy):
    """Guerreiro dragão que protege a câmara"""
    
    def __init__(self):
        super().__init__(
            name="Guerreiro Dragão",
            hp=100,
            attack=17,
            defense=9,
            xp_reward=280,
            description="Um guerreiro dragão que protege a câmara com sua força imensa."
        )
        self.can_flee = False