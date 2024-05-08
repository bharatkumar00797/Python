
class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        # Sort the scores in descending order
        sorted_scores = sorted(score, reverse=True)
        rank_dict = {}
        
        # Assign ranks
        for i, s in enumerate(sorted_scores):
            if i == 0:
                rank_dict[s] = "Gold Medal"  # Assign "Gold Medal" to the highest score
            elif i == 1:
                rank_dict[s] = "Silver Medal"  # Assign "Silver Medal" to the 2nd highest score
            elif i == 2:
                rank_dict[s] = "Bronze Medal"  # Assign "Bronze Medal" to the 3rd highest score
            else:
                rank_dict[s] = str(i + 1)  # Assign the numeric rank to other scores
        
        # Create the answer array
        answer = []
        for s in score:
            answer.append(rank_dict[s])  # Append the corresponding rank to the answer array
        
        return answer
