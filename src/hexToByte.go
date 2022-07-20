// You can edit this code!
// Click here and start typing.
package main

import (
	"fmt"
	"strings"
)

func main() {

   ciphertext := toByte("f03963DefABcD42b55060a6f688025b7de0b31777614ce174b835651843e301b64a52212d3226adc23a4545f1b204358bda427530920")
   // f(102) -a(97)+10
   fmt.Printf("%#x \n", ciphertext[0])
   fmt.Printf("%#x \n", ciphertext[1])
   fmt.Println('f' - 'a')
   //fmt.Printf("%#x", ciphertext[2])
   //fmt.Printf("%#x", ciphertext[1])
}

// Hex String to []byte 변환하기 (ASCII 테이블 참조)
//두개씩 더해 풀었다.
func toByte(s string) []byte {
   bs := []byte(strings.ToLower(s))
   b := make([]byte, len(bs)/2)

   if len(bs) == 0 {
      return []byte{}
   }

   for i := 0; i < len(s)/2; i++ {
      // 짝수 일때
      switch bs[i*2] {
      case '0', '1', '2', '3', '4', '5', '6', '7', '8', '9':
         b[i] = (bs[i*2] - '0') << 4 //0으로 빼면 형변환됌
         //fmt.Println("짝수 숫자")
         //fmt.Println(b[i])
      case 'a', 'b', 'c', 'd', 'e', 'f':
         //fmt.Println("짝수 영문")
        //  fmt.Println('f' - 'a')
         b[i] = (bs[i*2] - 'a' + 10) << 4 
      }

      // 홀수 일때
      switch bs[i*2+1] {
      case '0', '1', '2', '3', '4', '5', '6', '7', '8', '9':
         b[i] += (bs[i*2+1] - '0')
         //fmt.Println("홀수 숫자~")
      case 'a', 'b', 'c', 'd', 'e', 'f':
         b[i] += (bs[i*2+1] - 'a' + 10)
         //fmt.Println("홀수 영문~")
      }

	  fmt.Printf("%d %#x \n",i, b[i])
   }
   return b
}
