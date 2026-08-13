/*
- DISCIPLINA: Programação de Sistemas 2026
- ESTUDANTES: Artur Lacerda da Silva
- DATA      : 2026.08.13
- PROJETO   : aula32-projeto-secretaria
- ARQUIVO   : Aluno.java
*/

public class Aluno {
    private String nome;
    private String matricula;
    private String curso;


    public Aluno(String nome, String matricula, String curso){
        this.nome = nome;
        this.matricula = matricula;
        this.curso = curso;
    }
    
    public String getNome(){
        return nome;
    }
    public String getMatricula(){
        return matricula;
    }
    public String getCurso(){
        return curso;
    }

    public void setNome(String nome){
        this.nome = nome;
    }

    public void setCurso(String curso){
        this.curso = curso;
    }


}