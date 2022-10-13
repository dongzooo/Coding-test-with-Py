def solution(citations):
    citations.sort(reverse=True)
    article_count = len(citations)

    for i in range(article_count):
        if citations[i] <= i:
            return i
    return 0
