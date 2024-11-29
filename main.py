import pygame
import numpy as np


# Configurações do ambiente
WIDTH, HEIGHT = 500, 500 
GRID_SIZE = 50 
ROWS, COLS = HEIGHT // GRID_SIZE, WIDTH // GRID_SIZE 
BG_COLOR = (30, 30, 30) 
AGENT_COLOR = (255, 0, 0) 
FPS = 5 

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Agente com Ações Aleatórias")
clock = pygame.time.Clock()

def draw_grid():
    for x in range(0, WIDTH, GRID_SIZE):
        pygame.draw.line(screen, (50, 50, 50), (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, (50, 50, 50), (0, y), (WIDTH, y))

# Ambiente
class Environment:
    def __init__(self):
        self.agent_pos = np.array([ROWS // 2, COLS // 2]) 
    
    def reset(self):
        self.agent_pos = np.array([ROWS // 2, COLS // 2])
        return self.agent_pos

    def step(self, action):
        """Executa uma ação e atualiza o estado."""
        # Ações: 0 = cima, 1 = baixo, 2 = esquerda, 3 = direita
        if action == 0 and self.agent_pos[0] > 0:  # Cima
            self.agent_pos[0] -= 1
        elif action == 1 and self.agent_pos[0] < ROWS - 1:  # Baixo
            self.agent_pos[0] += 1
        elif action == 2 and self.agent_pos[1] > 0:  # Esquerda
            self.agent_pos[1] -= 1
        elif action == 3 and self.agent_pos[1] < COLS - 1:  # Direita
            self.agent_pos[1] += 1

        recompensa = 0  # Sem recompensa por enquanto
        feito = False  # Nunca termina nesse exemplo
        return self.agent_pos, recompensa, feito

# Agente
class RandomAgent:
    def __init__(self):
        pass

    def select_action(self):
        """Seleciona uma ação aleatória."""
        return np.random.choice([0, 1, 2, 3])

# Inicializando ambiente e agente
env = Environment()
agent = RandomAgent()

# Loop principal
running = True
state = env.reset()

while running:
    screen.fill(BG_COLOR)
    draw_grid()

    agent_rect = pygame.Rect(state[1] * GRID_SIZE, state[0] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
    pygame.draw.rect(screen, AGENT_COLOR, agent_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Agente escolhe uma ação aleatória e executa no ambiente
    action = agent.select_action()
    state, reward, done = env.step(action)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
