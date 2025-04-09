![Feito com Django](https://img.shields.io/badge/feito%20com-Django-092E20?style=for-the-badge&logo=django&logoColor=white)

> 💡 Sistema web para coachs/mentores gerenciarem alunos com tarefas, vídeos e agendamento de reuniões.

---
## 🛠️ Tecnologias Utilizadas
O projeto `Web-Coach` foi desenvolvido com uma combinação poderosa de ferramentas modernas para garantir performance, segurança, interatividade e um código limpo e manutenível.

## Back-end

- 🐍 **Python & Django**: estrutura robusta e escalável para criação de aplicações web rápidas e seguras.

- 🔒 `django.contrib.auth e auth.decorators`: utilizados para autenticação de usuários e proteção de rotas, garantindo que apenas usuários autorizados tenham acesso às funcionalidades da plataforma.

- 📆 `datetime`: utilizada para realizar cálculos e manipulação de datas, sendo essencial nas funcionalidades de agendamento de reuniões e organização de tarefas.

- 🔐 `secrets`: responsável por gerar tokens únicos e seguros para cada aluno. Foi implementada uma função personalizada com validações para evitar repetições (mesmo que a chance já seja muito baixa). A função save() também foi sobrescrita no modelo do aluno para que o token seja automaticamente atribuído ao ser criado.

## 🎨 Front-end

### 🧱 HTML + Tailwind CSS: estruturação visual com um sistema de utilitários altamente customizável, que oferece:

- Estilo limpo, moderno e responsivo.

- Desenvolvimento ágil com menos linhas de código CSS.

- ⚡ `HTMX`: permite interações dinâmicas com o backend sem a necessidade de JavaScript ou formulários complexos, deixando a navegação mais fluida e interativa.

- 📊 `Chart.js` (via CDN): biblioteca JavaScript utilizada para a exibição dos gráficos de pizza, trazendo informações visuais e intuitivas sobre os mentorados.

- O uso via CDN torna a integração mais rápida e reduz dependências no projeto.

## ✨ Benefícios do Stack

- Código mais simples, organizado e eficiente.

- Interface limpa e com boa experiência para o usuário.

- Menor dependência de arquivos estáticos pesados.

- Backend seguro e flexível, pronto para evoluir com o projeto.

---

## 📚 Sobre o Projeto

Este projeto foi desenvolvido com o objetivo de **aprimorar conhecimentos práticos** no uso do framework **Django**, aplicando tecnologias modernas para criar um sistema **simples, dinâmico e responsivo**.  

A proposta foi construir uma aplicação funcional com foco na **gestão entre coachs e seus mentorados**, servindo como uma base sólida para expandir funcionalidades e explorar novos recursos do ecossistema Django.

Durante o desenvolvimento, surgiram diversas oportunidades de melhorias e ideias para o crescimento do sistema — tanto em nível técnico quanto funcional.

---

## 🤝 Contribuições são bem-vindas!

Este repositório está **aberto para sugestões, melhorias e pull requests**!  
Se você tem ideias para funcionalidades, melhorias de código ou até otimizações de design, fique à vontade para contribuir.

> 💬 Sinta-se à vontade para abrir uma issue ou enviar um PR — toda ajuda será muito bem-vinda!

---

## 🧭 Funcionalidades Principais

### 👤 *Área do Coach*
- 🔐 Login e cadastro de coachs
  
  📸 *Tela de cadastro* 
  <p align="center">
  <img src="assets/projetocoach_cadastro.PNG" alt="Banner Web-Coach" style="max-width: 100%; height: auto;">
  </p>

  📸 *Tela de login* 
  <p align="center">
  <img src="assets/projetocoach_login.PNG" alt="Banner Web-Coach" style="max-width: 100%; height: auto;">
  </p>

- 📋 Listagem de alunos
- 📊 Gráfico de pizza com informações dos mentorados

  📸 *Tela de administração* 
  <p align="center">
  <img src="assets/projetocoach_mentorados.PNG" alt="Banner Web-Coach" style="max-width: 100%; height: auto;">
  </p>
  
- 📂 Tela de gerenciamento de cada aluno:
  - ✅ Cadastro de tarefas
  - 🎥 Upload de vídeos
  - ✔️ Marcar tarefas como concluídas
    
    📸 *Gerenciamento do aluno* 
  <p align="center">
  <img src="assets/projetocoach_mentorado.PNG" alt="Banner Web-Coach" style="max-width: 100%; height: auto;">
  </p>

- 🔑 Geração de token único para cada aluno
- 🔗 Criação de agenda de datas e horários disponíveis para reuniões

  📸 *Disponibilizar horários* 
  <p align="center">
  <img src="assets/projetocoach_reuniao.PNG" alt="Banner Web-Coach" style="max-width: 100%; height: auto;">
  </p>

---

### 🎓 *Área do Aluno*
- 🔐 Acesso via link + token disponibilizado pelo coach

  📸 *login do aluno* 
  <p align="center">
  <img src="assets/projetocoach_authmentorado.PNG" alt="Banner Web-Coach" style="max-width: 100%; height: auto;">
  </p>
  
- 📅 Escolha de dia para marcar reunião

  📸 *Dia da reunião* 
  <p align="center">
  <img src="assets/projetocoach_escolherdia.PNG" alt="Banner Web-Coach" style="max-width: 100%; height: auto;">
  </p>

- 🕒 Seleção de horários disponíveis

  📸 *Agendar reunião* 
  <p align="center">
  <img src="assets/projetocoach_agendarreuniao.PNG" alt="Banner Web-Coach" style="max-width: 100%; height: auto;">
  </p>

- 📑 Tela com todas as tarefas atribuídas
  - ✅ Checkbox para marcar como concluída
  - 🎞️ Visualização dos vídeos enviados pelo coach

📸 *Área do aluno* 
  <p align="center">
  <img src="assets/projetocoach_areamentorado.PNG" alt="Banner Web-Coach" style="max-width: 100%; height: auto;">
  </p>

---

### 🚀 Como rodar o projeto localmente

Siga os passos abaixo para clonar e executar este projeto na sua máquina:

---

### 📁 1. Clone o repositório

bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio


---

### 🧪 2. Crie e ative um ambiente virtual

bash
python -m venv venv
# No Windows:
venv\Scripts\activate
# No Linux/macOS:
source venv/bin/activate


---

### 📆 3. Instale as dependências

bash
pip install -r requirements.txt


---

### 🔐 4. Configure as variáveis de ambiente

Crie um arquivo .env na raiz do projeto com o seguinte conteúdo (baseado no .env.example):

env
SECRET_KEY=sua-chave-secreta-aqui
DEBUG=True


> Dica: Gere uma nova SECRET_KEY executando:

bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"


---

### 🚠 5. Aplique as migrações do banco de dados

bash
python manage.py migrate


---

### 👤 6. (Opcional) Crie um superusuário

bash
python manage.py createsuperuser


---

### ▶️ 7. Execute o servidor de desenvolvimento

bash
python manage.py runserver


Acesse o projeto em: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---
