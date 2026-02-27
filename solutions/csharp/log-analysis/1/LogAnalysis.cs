static class LogAnalysis
{
    public static string SubstringAfter(this string str, string delimiter) =>
        str.Substring(str.IndexOf(delimiter) + delimiter.Length);

    public static string SubstringBetween(this string str, string opening, string closing) =>
        str.SubstringAfter(opening).Substring(0, str.SubstringAfter(opening).IndexOf(closing));

    public static string Message(this string str) =>
        str.SubstringAfter(": ").Trim();

    public static string LogLevel(this string str) =>
        str.SubstringBetween("[", "]");
}