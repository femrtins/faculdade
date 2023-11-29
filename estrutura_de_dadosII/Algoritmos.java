import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;


public class Algoritmos {

    public int prim(Grafo grafo, Vertice raiz){
        Grafo arvore = new Grafo();
        int somaCusto = 0;

        for (Vertice v : grafo.vertices)
        {
            v.predecessor = null;
            v.chave = Integer.MAX_VALUE;
            arvore.insereV(v);
        }

        raiz.chave = 0;
        ArrayList<Vertice> Q = new ArrayList<Vertice>();

        for (Vertice a: grafo.vertices)
        {
            Q.add(a);
        }

        while (!(Q.isEmpty()))
        {
            Collections.sort(Q, Comparator.comparingInt(a -> a.chave));
            Vertice u = Q.remove(0);

            for (Vertice v : u.adj())
            {
                
                if((Q.contains(v)) && (grafo.getA(u, v).distancia < v.chave))
                {
                    v.predecessor = u;
                    v.chave = grafo.getA(u, v).distancia;
                    somaCusto += v.chave;
                    arvore.insereA(u, v, grafo.getA(u, v).distancia);
                }                                
            }
        }     
        arvore.imprime();  
        return somaCusto;
    }
}