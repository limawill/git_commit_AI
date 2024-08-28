import os
import subprocess
import google.generativeai as genai



genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')


def run_git_command(command):
    try:
        # Executa o comando git e captura a saída
        result = subprocess.run(
            command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o comando: {e}")
        print(f"Mensagem de erro: {e.stderr}")
        return None


output = run_git_command(["git", "diff"])

Teste = f"Analisar o retorno do comando git diff e criar uma frase de no maximo de 3 linhas focando na alterações do código para serem utilizadas no comando git commit: {
    output} "


response = model.generate_content(str(Teste))
print(response.text)

