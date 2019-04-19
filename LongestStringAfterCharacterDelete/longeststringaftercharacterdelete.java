/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package longeststringaftercharacterdelete;

/**
 *
 * @author Waseem
 */
import java.util.ArrayList;
import java.util.List;

/**
 * <p>
 * Giving a string and an string dictionary, find the longest string in
 * dictionary which can formed by deleting some characters of the giving string.
 * eg:S = abpcplea, Dict = {ale, apple, monkey, plea}, the return "apple"
 * </p>
 * 
 * @author 
 * 
 */

//Added few conditions to check if there are multiple longest string with same length.
public class LongestStringAfterCharacterDelete {

	List findLongestString(List<String> dict, String input) {

		String finalString = null;
		List<String> multipleLongestString = new ArrayList<String>();
		int index = 0;
		boolean isLongStringFound = false;
		for (String tempDict : dict) {

			finalString = compareString(tempDict, input);

			if (tempDict.equals(finalString)) {
				finalString = tempDict;
				if (multipleLongestString.size() == 0) {
					multipleLongestString.add(index, finalString);
				} else if (finalString.length() > multipleLongestString.get(0)
						.length()) {
					isLongStringFound = true;
				}
			}

			if (finalString.length() >= multipleLongestString.get(0).length()
					&& !finalString.equals(multipleLongestString.get(0))) {
				if (isLongStringFound) {
					multipleLongestString.remove(0);
					isLongStringFound = false;
				}
				multipleLongestString.add(0, finalString);
				index++;
			}
		}

		printList(multipleLongestString);

		return multipleLongestString;
	}

	void printList(List<String> inputList) {

		for (String longestString : inputList) {
			System.out.println(longestString);
		}

	}

	String compareString(String tempDict, String input) {

		StringBuffer sb = new StringBuffer();
		int tempCount = 0;
		int inputStringLength = input.length();
		int dictLength = 0;

		while (inputStringLength != 0) {

			if (dictLength < tempDict.length()) {
				if (input.toLowerCase().contains(
						Character.toString(tempDict.toLowerCase().charAt(
								tempCount)))) {

					sb.append(tempDict.charAt(tempCount));

					tempCount++;
					dictLength++;
				}
			}
			inputStringLength--;
		}

		return sb.toString();
	}

	public static void main(String[] args) {
		List<String> dict = new ArrayList<String>();
		dict.add("ale");
		dict.add("applee");
		dict.add("monkye");
		dict.add("plea");
                dict.add("abpDCsky");
		String input = "abpcpleeaDChsssgtrsssmonkey";
                System.out.println("String is "+input);
                System.out.println("dict is "+dict);
		LongestStringAfterCharacterDelete ls = new LongestStringAfterCharacterDelete();
                System.out.println("Answer is ");
		ls.findLongestString(dict, input);
	}

}
