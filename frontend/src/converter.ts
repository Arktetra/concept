export const mdToHtmlHeading = (text: string): string => {
    let re = /^(#+)\s*(.*)$/gm;

    return text.replace(re, (match, g1, g2) => {
        let level = g1.length;
        return `<h${level}>${g2}</h${level}>`;
    })
}

export const mdToHtmlBullets = (text: string): string => {
    let reUnorderedList = /^-\s(.*)$/gm;

    text = text.replace(reUnorderedList, (match, g1) => {
        return `<li>${g1}</li>`;
    });

    text = text.replace(/^(<li>.*\n[\s\S]*?)\n\n/gm, `<ul>\n$1\n</ul>\n\n`);

    return text;
}

export const mdToHtmlParagraph = (text: string): string => {
    let re = /^(?!(\s*$|<h.>|<ul>|<li>|<\/ul>))([\s\S]*?)$/gm;

    return text.replace(re, `<p>$2</p>\n`);
}

export const mdToHtml = (text: string): string => {
    text = mdToHtmlHeading(text);
    text = mdToHtmlBullets(text);
    text = mdToHtmlParagraph(text);
    return text;
}