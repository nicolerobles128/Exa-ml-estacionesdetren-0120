# Reporte de Análisis de Datos - Pandas

`Nicole Robles Machine Learning pandas, NC 0120`

## 1. DataFrame Convertido
```text
       Estacion  Trenes_dia  Pasajeros_dia
0    Buenavista          80         250000
1       Fortuna          60         180000
2      Lechería          50         120000
3        Toluca          45          90000
4   Insurgentes          70         200000
5  Observatorio          55         150000
```

## 2.1 Primeras Filas (head)
```text
     Estacion  Trenes_dia  Pasajeros_dia
0  Buenavista          80         250000
1     Fortuna          60         180000
```

## 2.2 Últimas Filas (tail)
```text
       Estacion  Trenes_dia  Pasajeros_dia
4   Insurgentes          70         200000
5  Observatorio          55         150000
```

## 2.3 Dimensiones (Filas, Columnas)
```text
(6, 3)
```

## 2.4 Tipos de Datos por Columna
```text
Estacion           str
Trenes_dia       int64
Pasajeros_dia    int64
dtype: object
```

## 2.5 Información General (info)
```text
<class 'pandas.DataFrame'>
RangeIndex: 6 entries, 0 to 5
Data columns (total 3 columns):
 #   Column         Non-Null Count  Dtype
---  ------         --------------  -----
 0   Estacion       6 non-null      str  
 1   Trenes_dia     6 non-null      int64
 2   Pasajeros_dia  6 non-null      int64
dtypes: int64(2), str(1)
memory usage: 276.0 bytes

```

## 3. Estadísticas Generales de la Columna 'Pasajeros_dia'
```text
count         6.000000
mean     165000.000000
std       57532.599455
min       90000.000000
25%      127500.000000
50%      165000.000000
75%      195000.000000
max      250000.000000
Name: Pasajeros_dia, dtype: float64
```

## 4. Ordenar Ascendente por Pasajeros_dia
```text
       Estacion  Trenes_dia  Pasajeros_dia
3        Toluca          45          90000
2      Lechería          50         120000
5  Observatorio          55         150000
1       Fortuna          60         180000
4   Insurgentes          70         200000
0    Buenavista          80         250000
```

## 5. Ordenar Descendente por Trenes_dia
```text
       Estacion  Trenes_dia  Pasajeros_dia
0    Buenavista          80         250000
4   Insurgentes          70         200000
1       Fortuna          60         180000
5  Observatorio          55         150000
2      Lechería          50         120000
3        Toluca          45          90000
```

`Nicole Robles Machine Learning pandas, NC 0120`