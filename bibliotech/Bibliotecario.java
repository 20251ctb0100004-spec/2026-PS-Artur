/*
 * Disciplina: 2026-PS
 * Projeto   : bibliotech
 * Arquivo   : Bibliotecario.java
 * Autor     : ARTUR LACERDA DA SILVA
 * Descricao : Bibliotecario E UM TIPO DE Usuario: herda nome, matricula e entrar().
 */
public class Bibliotecario extends Usuario {

    private String setor;

    public Bibliotecario(String nome, String matricula, String setor) {
        super(nome, matricula); // Inicializa a parte de Usuario (nome e matricula)
        this.setor = setor;
    }

    public String getSetor() {
        return setor;
    }

    public void setSetor(String setor) {
        this.setor = setor;
    }

    // Operacao de cadastrar livro/leitor (regra basica demonstrativa)
    public void cadastrarLivro() {
        System.out.println("Bibliotecário " + getNome() + " está cadastrando um novo livro.");
    }

    @Override
    public String toString() {
        return "Bibliotecário " + super.toString() + " - " + getMatricula() + ") - Setor: " + setor;
    }
}