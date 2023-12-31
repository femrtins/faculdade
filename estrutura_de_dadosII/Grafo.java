import java.util.ArrayList;
import java.util.List;

public class Grafo {

    public ArrayList<Vertice> vertices = new ArrayList<>();
    public ArrayList<Aresta> arestas = new ArrayList<>();
    public Grafo()
    
    {
        vertices = new ArrayList<Vertice>();
    }

    public Vertice insereV()
    {
        Vertice v = new Vertice();
        vertices.add(v);
        return v;
    }

    public void insereV(Vertice v)
    {
        vertices.add(v);
    }

    public Aresta insereA(Vertice v, Vertice u)
    {
        Aresta a = new Aresta(v, u);
        v.addAresta(a);
        u.addAresta(a);
        arestas.add(a);
        return a;
    }

    public Aresta insereA(Vertice v, Vertice u, int distancia)
    {
        Aresta a = new Aresta(v, u, distancia);
        v.addAresta(a);
        u.addAresta(a);
        arestas.add(a);
        return a;
    }

    public void removeV(Vertice v)
    {
        vertices.remove(v);
        for (Aresta x : v.listaArestas())
        {
            for (Vertice i : vertices)
            {
                for (Aresta j: i.listaArestas())
                {
                    if (x == j){
                        i.removeAresta(j);
                        arestas.remove(j);
                    }
                }
            }
        }        
    }

    public void removeA(Aresta e)
    {
        arestas.remove(e);
        for (Vertice i : vertices)
        {
            for (Aresta j: i.listaArestas())
            {
                if (e == j){
                    i.listaArestas().remove(j);
                }
            }
        }
    }

    public void vertices()
    {   
        int i = 0;
        System.out.print("<");
        for (Vertice v : vertices)
        {
            System.out.print(v.getId() + (i < vertices.size()-1 ? ", " : ""));
            i++;
        }
        System.out.print(">\n");
    }

    public void arestas()
    {   
        int i = 0;
        System.out.print("<");
        for (Aresta a : arestas)
        {
            System.out.print(a.getId() + (i < arestas.size()-1 ? ", " : ""));
            i++;
        }
        System.out.print(">\n");
    }

    public int getOrdem()
    {
        return vertices.size();
    }

    public int getTamanho()
    {
        return arestas.size();
    }

    public Aresta getA(Vertice v, Vertice u)
    {
        for (Aresta a : v.listaArestas())
        {
            for (Aresta b : u.listaArestas())
            {
                if(a == b){ return a; }                
            }
        }
        return null;
    }

    public int grau(Vertice v)
    {
        return v.listaArestas().size();
    }

    public List<Vertice> verticesA(Aresta e)
    {
        List<Vertice> par = new ArrayList<>();
        par.add(e.getVertice1());
        par.add(e.getVertice2());
        return par;
    }

    public Vertice oposto(Vertice v, Aresta e)
    {
        if (e.getVertice1() == v)
        {
            return e.getVertice2();
        }
        if (e.getVertice2() == v)
        {
            return e.getVertice1();
        }        
        return null;
    }



    public void imprime()
    {
        for (Aresta a: arestas)
        {
            System.out.print(a.getVertice1().getId() + " ── " + a.getVertice2().getId() + "\n");
        }
    }

    @Override
    public String toString()
    {
        String x = new String();
        for (Aresta a: arestas)
        {
            x += (a.getVertice1().getId() + " ── " + a.getVertice2().getId() + "\n");
        }
        return x;
    }
}