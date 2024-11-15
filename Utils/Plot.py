import plotly.graph_objects as go
from Utils.Constants import Constants

class Plot:
    @staticmethod
    def plot_execution_times(results):
        length_algorithms = len(Constants.ALGORITHMS)
        
        for size in Constants.SIZES:
            tiempos = []
            
            # Llenar la lista de tiempos según el tamaño de la matriz y el algoritmo
            for algorithm in Constants.ALGORITHMS:
                result = next((x for x in results if x.get_name() == algorithm), None)
                if result:
                    tiempo = result.get_time(f"{size}x{size}")
                else:
                    tiempo = 0
                tiempos.append(tiempo)
            
            # Crear el gráfico de columnas
            fig = go.Figure(data=[
                go.Bar(x=Constants.ALGORITHMS, y=tiempos)
            ])
            
            # Configuración del gráfico
            fig.update_layout(
                title=f"Tiempos de ejecución para el tamaño {size}x{size}",
                xaxis_title="Algoritmos",
                yaxis_title="Tiempo (ms)",
                margin=dict(l=50, r=50, t=50, b=50),
                width=1000,
                height=600
            )
            
            # Mostrar el gráfico
            fig.show()
