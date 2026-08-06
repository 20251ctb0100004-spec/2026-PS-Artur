public class menorValor {
    static int menorvalor(int[] numeros){
        int i = 0;
        menor = numeros[0];
        while(i<numeros.length){
            if(numeros[i]<menor){
                menor = numeros[i];
            }
            i++;
        }
    }
}