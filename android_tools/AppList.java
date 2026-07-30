import android.app.ActivityThread;
import android.content.Context;
import android.content.pm.ApplicationInfo;
import android.content.pm.PackageManager;

import java.util.List;

public class AppList {

    public static void main(String[] args) {

        Context context = ActivityThread.currentApplication();

        PackageManager pm = context.getPackageManager();

        List<ApplicationInfo> apps =
                pm.getInstalledApplications(
                    PackageManager.GET_META_DATA
                );


        for (ApplicationInfo app : apps) {

            String name =
                pm.getApplicationLabel(app).toString();

            System.out.println(
                name + "|" + app.packageName
            );
        }
    }
}
