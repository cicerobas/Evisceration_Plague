from code.Entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple[int, int]):
        super().__init__(name, position)
        self.is_attacking = False
        self.is_reload = False
        self.is_moving = False
        self.melee_attack = 1

        self.set_animation("Idle")

    def update(self, speed: float):
        if self.is_moving:
            self.set_animation("Walk")
        elif self.is_attacking:
            self.set_animation(f"Attack_{self.melee_attack}")
        elif self.is_reload:
            self.set_animation("Recharge")
        else:
            self.set_animation("Idle")

        # COOLDOWN = 100
        # if pygame.time.get_ticks() - self.update_time > COOLDOWN:
        #     self.update_time = pygame.time.get_ticks()
        #     self.current_frame += 1
        # if self.current_frame >= len(self.animation_frames):
        #     self.current_frame = 0
        # self.image = self.animation_frames[self.current_frame]
        self.current_frame += speed
        if int(self.current_frame) >= len(self.animation_frames):
            self.current_frame = 0
            if self.is_attacking:
                self.is_attacking = False
            if self.is_reload:
                self.is_reload = False

        self.image = self.animation_frames[int(self.current_frame)]

    def set_animation(self, name: str):
        if name != self.current_animation:
            self.animation_frames = self.animations.get_frames(name, self.direction == "L")
            self.current_animation = name

    def move(self, is_moving: bool, direction: str = ""):
        if is_moving:
            self.is_moving = True
            self.direction = direction
        else:
            self.is_moving = False

    def attack(self, is_attacking: bool):
        if is_attacking:
            self.is_moving = False
            self.is_attacking = True
            self.melee_attack = 1 if self.melee_attack == 2 else 2
        else:
            self.is_attacking = False
