# Para baixar as dependências no .m2
mvn install

# Para rodar as classes
mvn clean compile exec:java -Dexec.mainClass="br.com.comandocerto.playgrounds.Main"
mvn clean compile exec:java -Dexec.mainClass="br.com.comandocerto.playgrounds.SandboxCommonsText"
Ou clique na setinha de play no vscode