# Detecção de Mãos em Tempo Real com OpenCV e MediaPipe

Este é um projeto simples e eficiente em Python para detecção e mapeamento de mãos em tempo real utilizando a webcam do computador. O projeto utiliza a biblioteca **OpenCV** para captura e exibição de vídeo, e o **MediaPipe** da Google para a detecção de múltiplos pontos de articulação (landmarks) da mão.

---

## 🚀 Funcionalidades

- **Captura da Webcam**: Leitura automática de vídeo em tempo real.
- **Processamento de Imagem**: Conversão de frames para RGB de forma otimizada para o processamento.
- **Detecção Multimãos**: Identificação e rastreamento de pontos de articulação em tempo real.
- **Visualização Gráfica**: Desenho das conexões ósseas e pontos das mãos diretamente no vídeo da câmera.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **MediaPipe**: Framework robusto para detecção de pose e rastreamento de mãos em tempo real.
- **OpenCV**: Biblioteca para visão computacional e captura/manipulação de vídeo.

---

## 📦 Instalação e Configuração

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/alexdistegit/Projeto_deteccao_maos.git
   cd Projeto_deteccao_maos
   ```

2. **Crie e ative um ambiente virtual (recomendado):**
   - **No Windows:**
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - **No macOS/Linux:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🎮 Como Usar

Com o ambiente ativado e as dependências instaladas, execute o script principal:

```bash
python hand_detection.py
```

- Uma janela será aberta exibindo a imagem de sua webcam com a detecção de mãos ativa.
- Para encerrar o programa, basta pressionar a tecla **`q`** com a janela ativa.

---

## 📝 Licença

Este projeto está sob a licença MIT. Sinta-se livre para usar, modificar e distribuir.
