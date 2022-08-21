# Wave Soccer

Cloning brasfoot in Python with Hexagonal Architecture

### Game Legend

- Manager = tecnico (nós)
- Defensor = zagueiro
- Midfield = meio de campo
- Attacker = atacante
- Goalkeeper = goleiro

### Game Brain

- 1) Define team who starts with the ball
- 2) Choose a random Midfield to start with the ball

- 3) Player pass ball order:
    - Goalkeeper -> Defensor || shoot to middle/Attacker
    - Defensor -> Midfield
    - Midfield -> Attacker
    - Attacker -> Shoot to the goal

- 4) Pass/Shoot Intercepts:
    - Midfield intercept pass Midfield
    - Defensor intercept shoot Attacker
    - Attacker intercept pass Defensor
    - Goalkeeper defends shoot Attacker

- 5) Addictional points of players (max points: 30):
    - pass_points (All)
    - shoot_points (Attacker)
    - defense_goal_points (Goalkeeper)
    - intercept_pass (Defensor, Midfield, Attacker)

### run
```
sh run.sh
```

### tests
```
sh tests.sh
```