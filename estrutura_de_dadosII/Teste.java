public class Teste {

    public static void main(String[] args) {

        Grafo g = new Grafo();

        // --------------------- Inserir Vértices ---------------------
        Vertice v1 = g.insereV();
        Vertice v2 = g.insereV(); 
        Vertice v3 = g.insereV(); 
        Vertice v4 = g.insereV(); 

        // --------------------- Inserir Arestas ---------------------
        Aresta e1 = g.insereA(v1, v2);
        Aresta e2 = g.insereA(v1, v3);
        Aresta e3 = g.insereA(v3, v3);
        Aresta e4 = g.insereA(v2, v3);
        Aresta e5 = g.insereA(v1, v4);
        Aresta e6 = g.insereA(v1, v4);
        

        // --------------------- Métodos ---------------------
    
        System.out.println("getOrdem() g: " + g.getOrdem());
        System.out.println("getTamanho() g: " + g.getTamanho());
        g.vertices();
        g.arestas();

        v3.adj();

        System.out.println("getA() g: " + g.getA(v2, v3));
        System.out.println("getA() g: " + g.getA(v2, v4));
        System.out.println("grau(v) v2: " + g.grau(v2));
        System.out.println("verticesA(e) e3: " + g.verticesA(e3));
        System.out.println("oposto(v,e) v2: " + g.oposto(v1, e1));

        System.out.println(g);

        g.removeV(v1);
        g.removeA(e4);

        System.out.println(g);


        // --------------------- Grafo Dirigido ---------------------
        GrafoDirigido d = new GrafoDirigido();

        // --------------------- Inserir Vértices ---------------------
        Vertice u1 = d.insereV();
        Vertice u2 = d.insereV(); 
        Vertice u3 = d.insereV(); 
        Vertice u4 = d.insereV(); 

        // --------------------- Inserir Arestas ---------------------
        Aresta f1 = d.insereA(u2, u1);
        Aresta f2 = d.insereA(u1, u3);
        Aresta f3 = d.insereA(u3, u3);
        Aresta f4 = d.insereA(u2, u3);
        Aresta f5 = d.insereA(u1, u4);
        Aresta f6 = d.insereA(u4, u1);

        // --------------------- Métodos ---------------------

        System.out.println("grauE(v) u1: " + d.grauE(u1));
        System.out.println("grauS(v) u1: " + d.grauS(u1));
        d.arestasE(u2);
        d.arestasS(u2);

        System.out.println(d);
    }
}
