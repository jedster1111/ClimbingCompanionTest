window.onload = function () {

    document.getElementById("translate").addEventListener("click", function () {
        LoadText();
    })


    function LoadText() {
        var beforeText = document.getElementById("pigLatinInput").value;
        document.getElementById("pigLatinOutput").value = pigLatin(beforeText);
    }
    // switches first and last letters
    function switchFL(str) {
        //split the string into an array consiting of each individual word
        var words = str.split(" ");
        //console.log(words);
        //console.log(words[0])

        var firstChar, lastChar;


        for (i = 0; i < words.length; i++) {
            var word = words[i];
            var letters = word.split("");
            firstChar = letters[0];
            lastChar = letters[letters.length - 1];
            //console.log(firstChar + " " + lastChar);
            letters[0] = lastChar;
            letters[letters.length - 1] = firstChar;
            //word.join("");
            //console.log(letters);
            words[i] = letters.join("");
            //console.log("words[" + i + "] is " + words[i])
        }
        outputText = words.join(" ");
        return outputText;
    }

    //transform words into pig latin, doesn't react to grammar at the moment.
    function pigLatin(str) {
        console.log("pigLatin() is called")
        var words = str.split(" ");
        var firstChar, lastChar, word, letters;
        var vowels = ['a', 'e', 'i', 'o', 'u']
        for (i = 0; i < words.length; i++) {
            letters = words[i].split("");
            //console.log(vowels.indexOf(letters[i].toLowerCase()) !== -1);

            //if first lettter is vowel, just add "way" to end
            if (vowels.indexOf(letters[0].toLowerCase()) !== -1) {
                console.log("Letter " + letters[0] + " is a vowel");
                words[i] += "way";
                console.log(words[i]);
            }
                //if first letter is consonent, is the next a consonant?
            else {

                //no, then move to end and add ay
                var j = 0;
                var grpChar = '';
                console.log("letters length is " + letters.length);
                while ((vowels.indexOf(letters[j].toLowerCase()) == -1)) {

                    firstChar = letters[j];
                    console.log("letter [" + letters[j] + "] is a consonant");
                    grpChar += letters[j];
                    j++;
                    console.log(j);
                    console.log(grpChar);
                    if (j == letters.length) {
                        grpChar = letters[0];
                        j = 1;
                        console.log("break");
                        break;                      
                    }
                }
                grpChar += "ay";
                for (var k = 0; k < j; k++) {
                    letters[k] = "";
                }
                letters[letters.length - 1] += grpChar;
                console.log(letters);
                words[i] = letters.join("");
            }
            
        }
        outputText = words.join(" ");
        console.log(outputText);
        return outputText;
    }
}