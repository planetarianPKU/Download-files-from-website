# Download-files-from-website
Very simple python code to download data from website

Sometimes we need to download many files from a website. And these files are in the same format: we just click and download them.
If the sum of files is huge, I have no patience to do this. So i write a code.

Take the files from IRIS for example: http://ds.iris.edu/pub/userdata/wilber/
In that website we can see there are many directories. In the children directory named after the data applicant,there are many files that can be downloaded.
such as in http://ds.iris.edu/pub/userdata/wilber/sklee/2017-11-15-mww54-south-korea/sac_data/
we have many files like: http://ds.iris.edu/pub/userdata/wilber/sklee/2017-11-15-mww54-south-korea/sac_data/G.INU.00.BHE.Q.2017.319.052959.SAC

And we just need to watch it in the html format following these steps:
1.View webpage in source code format. Your brower may have that function and you may just click right and click "View webpage source code"option.
2.find all the tag named <herf>.
3.the links of files that can be downloaded is just after the <herf> and you can choose which to download by setting the end of files that you need.
4.Save all the links in a list and request one by one.
5.To improve the stability of download, you can add some time-out test and try-except method to jump over the error file and continue downloading the last files.

中文：

非常简单的python代码，可从网站下载数据

有时我们需要从网站下载许多文件。这些文件的格式相同：我们只需单击并下载它们。
如果文件总数很大，我将没有耐心执行此操作。所以我写了一个代码。

以IRIS中的文件为例：http://ds.iris.edu/pub/userdata/wilber/
在该网站中，我们可以看到有许多目录。在以数据申请者命名的子目录中，有许多文件可以下载。
例如在http://ds.iris.edu/pub/userdata/wilber/sklee/2017-11-15-mww54-south-korea/sac_data/
我们有许多文件，例如：http://ds.iris.edu/pub/userdata/wilber/sklee/2017-11-15-mww54-south-korea/sac_data/G.INU.00.BHE.Q.2017.319。 052959.SAC

我们只需要按照以下步骤以html格式观看它：
1.以源代码格式查看网页。您的浏览器可能具有该功能，您可以单击右键，然后单击“查看网页源代码”选项。
2.找到所有名为<herf>的标签。
3.可以下载的文件链接位于<herf>之后，您可以通过设置所需文件的结尾来选择要下载的文件。
4.将所有链接保存在列表中，然后一个接一个地请求。
5.为提高下载的稳定性，您可以添加一些超时测试和try-except方法来跳过错误文件并继续下载最后一个文件
