# Genoma Processos

App da Genoma Consultoria Empresarial para **criar, melhorar e treinar** processos dos clientes. É um único arquivo HTML: abra `index.html` no navegador e use. Não precisa de instalação nem de servidor.

## O que faz

| Módulo | Para quê |
|---|---|
| **Painel** | Maturidade média, % da equipe treinada, tarefas abertas e atrasadas, esteira de fases, mural de decisões e modificações, próximos passos sugeridos |
| **Processos (POP)** | Criação do POP no padrão Genoma (código, RACI por etapa, passo a passo com decisões sim/não, fluxograma automático, assinaturas). Seis modelos prontos. Toda edição gera nova versão com histórico. Imprimir/PDF |
| **Treinamento** | Matriz pessoa × processo, estudo guiado etapa por etapa e avaliação gerada automaticamente do POP (aprovação a partir de 70%) |
| **Melhoria** | Indicadores com meta e medições, ideias da equipe (Ideia → Testando → Aprovada) e checklist de maturidade com a próxima ação sugerida |
| **Delegações** | Quadro de tarefas com processo a seguir, etapa, responsável e prazo. Os cartões podem ser arrastados entre colunas |
| **Decisões** | Registro de cada decisão com o processo afetado e quem executa |
| **Automações** | 8 regras que podem ser ligadas e desligadas (veja abaixo) |
| **Equipe** | Pessoas e cargos. O cargo liga a pessoa aos POPs e treinamentos dela |

Atende vários clientes: troque de cliente pelo seletor no topo.

### Automações

1. Decisão registrada → cria a delegação para o responsável
2. Processo criado → cria treinamentos para quem tem o cargo executor
3. Nova versão do POP → marca quem já foi treinado para retreinar
4. Avaliação concluída → registra como treinado (nota a partir de 70%) ou manda refazer
5. Todos os executores treinados → processo avança para "Implantado e treinado"
6. Medição fora da meta → abre uma melhoria e delega a análise
7. Delegação vencida → destaca e avisa no mural
8. Data de revisão do POP chegou → cria a tarefa de revisão (intervalo configurável)

## Dados

Os dados ficam salvos no navegador de quem usa (`localStorage`). Use **Baixar cópia de segurança** e **Restaurar cópia** para guardar ou levar os dados para outro computador. Para várias pessoas usarem os mesmos dados ao mesmo tempo, o próximo passo é publicar com uma base compartilhada.

O app vem com os dados da Mega Freio: POP-OPE-01 Controle de Produção, POP-DIR-02 Controle de Pátio e a decisão de 11/11/2026 sobre o canal de decisões e delegações.

## Desenvolvimento

- Código-fonte: `src/app.html`
- Logos oficiais (de genomaconsultoria.com): `assets/`
- Gerar o `index.html` com os logos embutidos: `python3 build.py`
