package br.com.comandocerto.playgrounds;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import lombok.ToString;

@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
@ToString
public class SandboxLombok {
    private String nome;

    public static void main(String[] args) {
        // Construtor atendido pela anotação @AllArgsConstructor.
        SandboxLombok sandboxLombok = new SandboxLombok("Jhonata");
        // Construtor atendido pela anotação @NoArgsConstructor.
        SandboxLombok sandboxLombok2 = new SandboxLombok();

        // Como estou dentro do arquivo da classe, consigo acessar
        // o atributo diretamente. Mas fora deste arquivo SandboxLombok só
        // conseguirá pelo setNome().
        sandboxLombok.nome = "Beatriz";
        System.out.println(sandboxLombok.nome);

        // Método setNome tendido pela anotação @Setter.
        sandboxLombok.setNome("Jesus");
        System.out.println(sandboxLombok.getNome());

        // Null pois usou construtor vazio.
        System.out.println(sandboxLombok2.nome);

        // Torna o toString mais legível, disso:
        //   br.com.comandocerto.playgrounds.SandboxLombok@1dbd16a6
        // para isso:
        //   SandboxLombok(nome=Jesus)
        System.out.println(sandboxLombok.toString());
    }
}
