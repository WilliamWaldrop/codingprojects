module hello-world where

open import IO

main = run (putStrln "Hello, World!")
