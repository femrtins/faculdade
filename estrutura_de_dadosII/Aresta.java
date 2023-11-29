public class Aresta{
    
    public static int proximoId = 1;
    private int id;
    private Vertice v1;
    private Vertice v2;
    public int chave;

    public int distancia;

    public Aresta(Vertice v1, Vertice v2)
    {
        id = proximoId++;
        this.v1 = v1;
        this.v2 = v2;
        this.distancia = 1;
    }

    public Aresta(Vertice v1, Vertice v2, int distancia)
    {
        id = proximoId++;
        this.v1 = v1;
        this.v2 = v2;
        this.distancia = distancia;
    }
    
    public Aresta inverte()
    {
        Aresta a = new Aresta(v2, v1);
        return a;
    }

    public int getId()
    {
        return id;
    }

    public Vertice getVertice1()
    {
        return v1;
    }

    public Vertice getVertice2()
    {
        return v2;
    }
}