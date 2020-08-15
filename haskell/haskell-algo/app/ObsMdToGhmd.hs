module ObsMdToGhmd where

import qualified Data.Text as T
import qualified Data.Text.IO as T
import qualified Text.Replace as RT
import Data.Void
import Replace.Megaparsec
import Text.Megaparsec
import Text.Megaparsec.Char
import Text.Megaparsec.Char.Lexer
import System.Directory
import System.FilePath.Posix


-- What I actaully want to do is read the whole dir, and collect image filesw
--  then read all the md files ... search for [[*.png]] in the text and replace that
-- Take a file, reformat the images and write back to disk
-- also i will have to copy all the image to destination dir and remove spaces
-- remove spaces from the image


-- processMdFile :: FilePath -> FilePath -> IO ()
processMdFile :: FilePath -> [Char] -> IO [()]
processMdFile src dest = do
    filesdir <- getDirectoryContents src 
    _ <- removeDirectoryRecursive $ dest 
    _ <- createDirectory $ dest
    _ <- createDirectory $ dest ++ "/images/"
    mapM (\f -> copyFile (src ++ "/" ++ f) (dest ++ "/images/" ++ rScore f)) (images filesdir)
    mapM (\f -> reformatImage (src ++ "/" ++ f) (dest ++ f)) (mdFiles filesdir)
    
    where 
        mdFiles = filter (\f ->  (takeExtension f) == ".md" )
        images = filter (\f ->  (takeExtension f) == ".png" )

reformatImage :: FilePath -> FilePath -> IO ()
reformatImage src destFile = do
    mdFileText <-  T.readFile src
    let bracevar = chunk "[[" *> manyTill anySingle (chunk ".png]]") :: Parsec Void String String
    T.writeFile destFile $ T.pack $ streamEdit bracevar (\p -> "[" ++ rScore p ++ "]" ++ "(" ++ "/hs-process/images/" ++ (rScore p)  ++ ".png)") $ T.unpack mdFileText
        

rScore :: String -> String
rScore str = 
    streamEdit space (const "_") str
    where 
        space = chunk " " :: Parsec Void String String
