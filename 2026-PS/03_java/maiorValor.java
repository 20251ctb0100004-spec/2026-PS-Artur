public class maiorValor {
    static int maiorvalor(int[] numeros){
        int i = 0;
        maior = numeros[0];
        while(i<numeros.length){
            if(numeros[i]<maior){
                maior = numeros[i];
            }
            i++;
        }
    }
}