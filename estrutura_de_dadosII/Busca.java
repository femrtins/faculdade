import java.util.LinkedList;
import java.util.Queue;

public class Busca {

    static int tempo = 0;

    public void buscaEmLargura(Grafo grafo, Vertice inicial)
    {
        for (Vertice v : grafo.vertices)
        {
            v.estado = "NAO_VISITADO";
            v.predecessor = null;
            v.distancia = Integer.MAX_VALUE;
        }

        inicial.distancia = 0;
        inicial.estado = "VISITADO";
        Queue<Vertice> fila = new LinkedList<Vertice> (); 
        fila.add(inicial);

        while (!(fila.isEmpty()))
        {
            Vertice vi = fila.poll();
            for (Vertice vj : vi.adj())
            {
                if (vj.estado == "NAO_VISITADO")
                {
                    fila.add(vj);
                    vj.estado = "VISITADO";
                    vj.predecessor = vi;
                    vj.distancia = vi.distancia + 1;
                }
            }
            vi.estado = "ENCERRADO";
        }
    }

    public void buscaEmProfundidade(Grafo grafo, Vertice inicial)
    {
        for (Vertice v : grafo.vertices)
        {
            v.estado = "NAO_VISITADO";
            v.predecessor = null;
        }

        for (Vertice v: grafo.vertices)
        {
            if (v.estado == "NAO_VISITADO")
            {
                visitaVertice(inicial);
            }
        }
    }

    private void visitaVertice(Vertice v)
    {
        v.estado = "VISITADO";
        tempo = tempo + 1;
        v.ta = tempo;

        for (Vertice vj : v.adj())
        {
            if(vj.estado == "NAO_VISITADO")
            {
                vj.predecessor = v;
                visitaVertice(vj);
            }
        }
        v.estado = "ENCERRADO";
        tempo = tempo + 1;
        v.te = tempo;
    }

    public void BuscaProfTodos(Grafo grafo)
    {
        for (Vertice v : grafo.vertices)
        {
            v.estado = "NAO_VISITADO";
            v.predecessor = null;
        }

        for (Vertice v : grafo.vertices)
        {
            if (v.estado == "NAO_VISITADO")
            {
                visitaVertice(v);
            }
        }
    }

    public void ImprimeCaminho(Grafo grafo, Vertice raiz, Vertice v){
        if (v==raiz)
        {
            raiz.imprime();
        }

        else
        {  
            if (v.predecessor == null)
            {
                System.out.println("Não existe caminho de r para v");    
            }
            else
            {
                ImprimeCaminho(grafo, raiz, v.predecessor);
                v.imprime();
            }
        }
    }

    private void CriaConjunto(Vertice v)
    {
        v.predecessor = v;
        v.peso = 0;
    }

    private Vertice BuscaConjunto(Vertice v)
    {
        Vertice p = v.predecessor;        
        if (v != p)
        {
            v.predecessor = BuscaConjunto(p);
        }
        return v.predecessor;
    }

    private void Uniao(Vertice u, Vertice v)
    {
        Link(BuscaConjunto(u), BuscaConjunto(v));
    }

    private void Link(Vertice u, Vertice v)
    {
        if (u.peso > v.peso)
        {
            v.predecessor = u;
        }
        else
        {
            u.predecessor = v;
            if (u.peso == v.peso)
            {
                v.peso = v.peso + 1;
            }
        }
    }

    private void ComponentesConexasConjuntos(Grafo grafo)
    {
        for (Vertice v: grafo.vertices)
        {


            CriaConjunto(v);
        }
        for (Aresta a: grafo.arestas)
        {
            Vertice u = a.getVertice1();
            Vertice w = a.getVertice2();
            if (BuscaConjunto(u) != BuscaConjunto(w))
            {
                Uniao(u, w);
            }
        }
    }

    private boolean MesmaComponente(Vertice u, Vertice v)
    {
        if (BuscaConjunto(u) == BuscaConjunto(v))
        {
            return true;
        }
        return false;
    }

    public String Conexidade(Grafo grafo)
    {
        ComponentesConexasConjuntos(grafo);

        for (int i = 0; i < grafo.vertices.size()-1; i++)
        {
            if (!MesmaComponente(grafo.vertices.get(i), grafo.vertices.get(i+1)))
            { return "Grafo Não Conexo";}
        }
        return "Grafo Conexo";
    }
}