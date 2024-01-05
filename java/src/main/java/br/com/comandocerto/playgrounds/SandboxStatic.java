package br.com.comandocerto.playgrounds;

public class SandboxStatic {
    // A palavra-chave static em Java é utilizada para
    // criar membros de classe que pertencem à própria classe,
    // em vez de pertencerem a instâncias específicas dessa classe.
    // Existem duas principais utilizações da palavra-chave static
    // em Java: membros estáticos e métodos estáticos.
    static int id = 10;
    static void PrintDoMeuNome() {
        System.out.println("Jhonata");
    }

    public static void main(String[] args) {
        // Não há necessidade de instanciar, pois o método e
        // o atributo são estáticos, percente à classe.
        System.out.println(SandboxStatic.id);
        SandboxStatic.id = 11;
        System.out.println(SandboxStatic.id);
        SandboxStatic.PrintDoMeuNome();
    }
}
